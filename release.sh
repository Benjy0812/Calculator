#!/bin/bash

# Make sure you're on the correct branch (e.g., main)
git checkout main

# Commit your changes if any
git add .
git commit -m "Release version $(date +'%Y-%m-%d')"  # Add a commit message or version

# Create a new tag based on the version or date
git tag "v$(date +'%Y.%m.%d.%H%M')"  # You can use your versioning scheme

# Push the changes and the tag
git push origin main
git push origin --tags  # Push both the commit and the tag
