import os 

def func_main():
    print('Wich setup do you want to run?')
    print('1. Laravel with tailwind')
    print('2. Laravel with tailwind and debugbar')
    print('3. Laravel')

    setup = input('Enter the number of the setup: \n')

    if setup == '1':
        os.system('laravel new ' + input('Enter the name of the project: '))
        os.system('cd ' + input('Enter the name of the project: '))
        # install tailwind
        os.system('npm install -D tailwindcss@latest postcss@latest autoprefixer@latest')
        os.system('npx tailwindcss init -p')
    elif setup == '2':
        os.system('laravel new ' + input('Enter the name of the project: '))
        os.system('cd ' + input('Enter the name of the project: '))
           # install tailwind
        os.system('npm install -D tailwindcss@latest postcss@latest autoprefixer@latest')
        os.system('npx tailwindcss init -p')
        # install debugbar
        os.system('composer require barryvdh/laravel-debugbar --dev')
        os.system('php artisan vendor:publish --provider="Barryvdh\Debugbar\ServiceProvider"')
        os.system('php artisan config:cache')
    elif setup == '3':
        os.system('laravel new ' + input('Enter the name of the project: '))
        os.system('cd ' + input('Enter the name of the project: '))
    else:
        print('Invalid input')


func_main()
