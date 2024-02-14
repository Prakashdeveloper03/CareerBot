#!/bin/bash

if [ ! -d "./assets" ]; then
    echo "Error: 'assets' directory not found."
    exit 1
fi

output_dir="./extracted"
mkdir -p "$output_dir"

processed_files=0
failed_files=0

for pdf_file in "./assets"/*.pdf; do
    if [ ! -f "$pdf_file" ]; then
        echo "Error: File not found: $pdf_file"
        ((failed_files++))
        continue
    fi

    filename=$(basename "$pdf_file" .pdf)
    txt_file="$output_dir/$filename.txt"

    if pdftotext "$pdf_file" "$txt_file"; then
        echo "Extracted text from: $pdf_file"
        ((processed_files++))
    else
        echo "Error: Failed to extract text from: $pdf_file"
        ((failed_files++))
    fi
done

echo "Summary:"
echo "Processed files: $processed_files"
echo "Failed files: $failed_files"
