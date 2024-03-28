import csv
import logging
from tqdm import tqdm
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def sanitize_document_id(document_id):
    """
    Sanitize the document ID by converting it to lowercase and replacing special characters.

    Args:
        document_id (str): The original document ID.

    Returns:
        str: The sanitized document ID.
    """
    return (
        document_id.lower()
        .replace(" ", "_")
        .replace(".", "")
        .replace("#", "_")
        .replace("/", "_")
    )


def upload_csv_to_firestore(csv_file_path, collection_name, id_field, fields_mapping):
    """
    Upload data from a CSV file to a Firestore collection.

    Args:
        csv_file_path (str): Path to the CSV file.
        collection_name (str): Name of the Firestore collection.
        id_field (str): Field in CSV representing unique identifiers for documents in Firestore.
        fields_mapping (dict): Mapping of CSV fields to Firestore fields.
    """
    try:
        # Open CSV file
        with open(csv_file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            total_rows = sum(1 for _ in reader)  # Get total number of rows
            file.seek(0)  # Reset file pointer
            reader = csv.DictReader(file)  # Reinitialize reader
            # Iterate over rows in the CSV file
            for row in tqdm(
                reader, total=total_rows, desc=f"Uploading '{csv_file_path}'"
            ):
                # Get document ID from CSV row and sanitize it
                document_id = sanitize_document_id(row[id_field])
                # Get reference to Firestore document
                doc_ref = db.collection(collection_name).document(document_id)
                data = {}
                # Map CSV fields to Firestore fields
                for firestore_field, csv_field in fields_mapping.items():
                    data[firestore_field] = row.get(csv_field, "")
                # Set data in Firestore document
                doc_ref.set(data)
        # Print success message
        tqdm.write(
            f"CSV file '{csv_file_path}' uploaded to Firestore collection '{collection_name}' successfully!"
        )
    except Exception as e:
        # Log error if upload fails
        logger.error(
            f"Failed to upload CSV file '{csv_file_path}' to Firestore collection '{collection_name}': {e}"
        )


# Define mappings for CSV files to Firestore collections
csv_mappings = [
    {
        "csv_file_path": "../data/courses.csv",
        "collection_name": "courses",
        "id_field": "course_title",
        "fields_mapping": {
            "course_organization": "course_organization",
            "course_certificate_type": "course_certificate_type",
            "course_time": "course_time",
            "course_rating": "course_rating",
            "course_reviews_num": "course_reviews_num",
            "course_difficulty": "course_difficulty",
            "course_url": "course_url",
            "course_students_enrolled": "course_students_enrolled",
            "course_skills": "course_skills",
            "course_summary": "course_summary",
            "course_description": "course_description",
        },
    },
    {
        "csv_file_path": "../data/keywords.csv",
        "collection_name": "skills",
        "id_field": "title",
        "fields_mapping": {"title": "title", "skills": "skills"},
    },
]

# Upload data from CSV files to Firestore collections
for mapping in csv_mappings:
    upload_csv_to_firestore(
        mapping["csv_file_path"],
        mapping["collection_name"],
        mapping["id_field"],
        mapping["fields_mapping"],
    )
