#!/bin/bash

echo "Which setup do you want to run?"
echo "1. Laravel with tailwind"
echo "2. Laravel with tailwind and debugbar"
echo "3. Laravel"

read -p "Enter the number of the setup: " setup

if [ "$setup" = "1" ]; then
    read -p "Enter the name of the project: " project_name
    laravel new "$project_name"
    cd "$project_name"
    # install tailwind
    npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
    npx tailwindcss init -p
elif [ "$setup" = "2" ]; then
    read -p "Enter the name of the project: " project_name
    laravel new "$project_name"
    cd "$project_name"
    # install tailwind
    npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
    npx tailwindcss init -p
    # install debugbar
    composer require barryvdh/laravel-debugbar --dev
    php artisan vendor:publish --provider="Barryvdh\Debugbar\ServiceProvider"
    php artisan config:cache
elif [ "$setup" = "3" ]; then
    read -p "Enter the name of the project: " project_name
    laravel new "$project_name"
    cd "$project_name"
else
    echo "Invalid input"
fi
