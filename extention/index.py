from sharpe import main
from sharpe import calculoPrivados
from sharpe import calculoPublico
import numpy as np
from tqdm import tqdm
from time import sleep

for i in tqdm(calculoPrivados):
    sleep(0.0001)