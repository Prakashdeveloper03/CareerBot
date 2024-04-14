# LaTeX Compilation Guide

This guide provides step-by-step instructions on how to compile this LaTeX document using `lualatex`.

## Prerequisites

Make sure you have LaTeX installed on your machine.
If not, you can install it by following the steps below:

## Installation Steps:

### Step 1: Update Package Lists

First, update the package lists to ensure you have the latest information about available packages:

```bash
# Debian/Ubuntu
sudo apt update -y

# Fedora/RPM
sudo dnf check-update -y

# Arch Linux
sudo pacman -Sy
```

### Step 2: Upgrade Installed Packages

Next, upgrade the installed packages to the latest versions available:

```bash
# Debian/Ubuntu
sudo apt upgrade -y

# Fedora/RPM
sudo dnf upgrade -y

# Arch Linux
sudo pacman -Su
```

### Step 3: Install texlive-latex-base Package

Now, install the `texlive-latex-base` package, which includes essential LaTeX files for basic document preparation:

```bash
# Debian/Ubuntu
sudo apt-get install texlive-latex-base -y

# Fedora/RPM
sudo dnf install texlive-latex-base -y

# Arch Linux
sudo pacman -S texlive-latex-base --noconfirm
```

### Step 4: Install texlive-latex-extra Package

Additionally, install the `texlive-latex-extra` package, which contains extra LaTeX packages and tools for extended document preparation:

```bash
# Debian/Ubuntu
sudo apt-get install texlive-latex-extra -y

# Fedora/RPM
sudo dnf install texlive-latex-extra -y

# Arch Linux
sudo pacman -S texlive-latex-extra --noconfirm
```

### Step 5: Install texlive-science Package

Install the `texlive-science` package, which provides additional LaTeX packages tailored for scientific typesetting:

```bash
# Debian/Ubuntu
sudo apt-get install texlive-science -y

# Fedora/RPM
sudo dnf install texlive-science -y

# Arch Linux
sudo pacman -S texlive-science --noconfirm
```

### Step 6: Install on Windows

If you're using Windows, you can install LaTeX by setting up Windows Subsystem for Linux (WSL) and then following the steps mentioned above for Debian/Ubuntu.

Alternatively, you can download and install TeX Live from the official website.

## Compilation Process

### Step 1: Clone the Repository

Clone the project repository to your local machine using the following command:

```bash
git clone https://github.com/Prakashdeveloper03/CareerBot.git
```

### Step 2: Navigate to the Project Directory

Navigate to the directory containing LaTeX project files using the `cd` command:

```bash
cd latex/report
```

### Step 3: Compile Bibliography

Use the following command to compile the bibliography separately:

```bash
bibtex authesis
```

### Step 3: Compile the LaTeX Document

Execute the following command to compile the LaTeX document using `lualatex`:

```bash
lualatex authesis.tex
```

### Step 4: View the PDF Output

Once the compilation process is complete without errors, you can view the PDF output using your preferred PDF viewer. The compiled PDF file will usually be generated in the same directory as `authesis.pdf`.
