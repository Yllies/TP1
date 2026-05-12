"""
Logger centralisé pour les tests.
"""

import logging
import os
from datetime import datetime

# Créer le dossier de logs s'il n'existe pas
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


def setup_logger(name: str = "test", log_file: str = None) -> logging.Logger:
    """
    Configure un logger.
    """
    if not log_file:
        log_file = f"{LOG_DIR}/test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Éviter les duplicatas de handlers
    if logger.hasHandlers():
        logger.handlers.clear()
    
    # Format personnalisé
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)-8s | %(message)s',
        datefmt='%H:%M:%S'
    )
    
    # Handler fichier
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Handler console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    logger.info(f"Logger OK: {log_file}")
    return logger


# Logger par défaut
logger = setup_logger()
