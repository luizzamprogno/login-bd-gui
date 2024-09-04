from database import *
from gui import *

def main():
    
    conexao = create_connection()
    cursor = define_cursor(conexao)
    create_table(conexao, cursor)
    init_gui()

if __name__ == '__main__':
    main()