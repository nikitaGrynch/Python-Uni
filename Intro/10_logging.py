import logging
import i10_module

def main() -> None:
    logging.basicConfig(
        filename="logs.txt",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s [%(filename)s::%(lineno)d] - %(message)s %(args)s",
        datefmt="%d-%m-%Y %H:%M:%S")
    
    #logging.warning("This is a warning")
    logging.error("DAO error", {'sql': 'SELECT *',
                                'err': 'Syntax error'})
    i10_module.log_warning()

if __name__ == "__main__":
    main()