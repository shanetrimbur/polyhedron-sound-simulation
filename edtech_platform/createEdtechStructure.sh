#!/bin/bash

# Set up the project directory
mkdir -p edtech-platform
cd edtech-platform

# Create main folders
mkdir -p backend/models
mkdir -p backend/routes
mkdir -p backend/config
mkdir -p backend/middleware
mkdir -p frontend/src/components
mkdir -p frontend/src/pages
mkdir -p frontend/src/assets
mkdir -p scripts
mkdir -p infrastructure

# Create backend files
touch backend/server.js
touch backend/config/database.js
touch backend/models/User.js
touch backend/models/Course.js
touch backend/routes/auth.js
touch backend/routes/courses.js
touch backend/middleware/auth.js
touch backend/.env

# Create frontend files
touch frontend/package.json
touch frontend/src/index.js
touch frontend/src/App.js
touch frontend/src/components/Header.js
touch frontend/src/components/Footer.js
touch frontend/src/pages/Home.js
touch frontend/src/pages/Login.js
touch frontend/src/assets/logo.png

# Create infrastructure files
touch infrastructure/terraform.tf
touch infrastructure/variables.tf
touch infrastructure/outputs.tf

# Create script files
touch scripts/deploy.sh
touch scripts/start.sh

# Initialize README and other documentation
touch README.md
touch LICENSE

# Display the created structure
echo "Folder and file structure created successfully."
tree .

