#Angelo Flores 11.19.24
#init
import random
pokemon_level=0
pokemon_name="Charmander"
day=1

#Pokemon
#Functions
def draw_charmander():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠖⠋⠁⠀⠀⠀⠀⠉⠙⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣿⠂⠀⠀⠀⠀⠀⠀⠀⢀⡴⣆⡀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠛⣿⣆⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣟⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⣼⣿⣿⡆⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⢿⡇⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢯⡛⠋⣉⣼⠃⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣧⡀⠀⠐⡦⠀⢀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠀⢽⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⣤⡀⠀⠘⢿⣶⣄⣀⣀⠈⠁⠀⢀⣀⣀⣀⣀⣀⡤⠴⣾⠋⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⢿⣷⠀⠀⠀⠀
⠀⣠⣿⡉⠓⢦⣈⢯⡻⣷⠈⠉⠉⠉⠉⠀⠀⠀⣼⣇⡤⠊⣁⠼⠀⠀⠘⡇⠀⠀⢀⣀⡠⠴⠚⠋⣹⠟⠀⠀⠀⠀⠀⠀⢀⢸⠁⠀⠀⠈⢇⣤⠀⠀
⠸⣿⠋⢏⠉⠀⠈⠉⠛⢯⡳⠦⢤⣤⣤⡤⠴⢒⣋⣭⣖⠊⠁⠀⠀⠘⠒⠛⠒⠋⠉⠉⠀⠀⠒⣾⠻⣶⡆⠀⠀⠀⠀⠀⠀⢺⣧⡀⣤⠀⠸⣿⠀⠀
⠀⠈⠻⣎⠀⠀⠀⠀⠀⠀⠉⢹⡶⠒⠛⠉⠉⠉⠁⠀⠈⠳⣄⠳⣄⠀⠀⠀⠀⠀⡞⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⠀⠈⣧⡏⠀⣻⡆
⠀⠀⠀⠀⠀⠙⢧⣀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢁⡴⠟⠀⠀⠀⠀⠀⠀⠀⢘⡇⣿⢿⠀⢀⠈⣧⠀
⠀⠀⠀⠈⣠⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠿⢷⡀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠳⢤⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⠀⠀⠉⠉⠹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠈⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⢴⠖⡶⠟⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⡏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⢀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⣼⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠛⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣈⣤⡤⢤⣀⢸⠓⠶⢤⣀⣀⣀⣀⡤⠶⠚⠉⠀⠀⠀⢠⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠘⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠦⣄⣀⠀⠀⣀⡼⠃⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠉⠉⠙⠛⣆⠀⠀⠀⠀⠀⠀⠀⠀⣾⣥⣤⣀⣀⣀⣀⣠⡤⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⡴⠖⠉⠁⠀⠀⠀⠀⠀⠀⠀⢸⣁⠀⠀⠀⠀⠀⣹⡆⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⢿⣯⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡿⠀⠀⠀⠀⢀⡏⠁⠀⠀⠀⠀⢘⡉⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠻⠿⠿⠟⠷⠶⠶⠶⠶⠶⠒⠒⠒⠉⠉⠀⠀⠀⠀⠀⠀⢿⡟⠙⣶⠏⢳⣞⢙⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣟⡷⠟⣻⠛⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
#draws charmander
def draw_charmeleon():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠖⠋⠀⢀⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠖⠋⠀⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⠚⠉⠉⠁⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣟⢀⠀⠀⠀⡆⠀⠀⢀⡤⢿⡀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣼⠀⠀⠆⡇⢀⣿⣿⡇⠐⡇⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏⠀⠀⠀⠙⠯⠿⠟⠗⠚⠁⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⣷⢦⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠐⠃⢀⣠⣤⣤⣤⣠⡤⠞⠃⠀⡰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣼⡆⢹⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠲⠤⢾⡉⠀⠀⣀⣠⣤⡤⠀⠀⠀⠁⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⢧⡟⢸⠀⢶⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣹⠷⢾⠋⠀⠀⠀⠀⠰⢿⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠸⠶⠾⢸⢧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡠⠴⠊⠁⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⢠⣾⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡴⠟⠁⠀⠀⠀⠀⠀⠀⣠⠟⠉⠉⠓⢆⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠦⢄⡀⠀⠀⠀⠀⣠⠠⣳⠀⠀⠀⠀⢿⣿⡿⣄⠀
⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⣀⣠⠤⣾⠋⠀⠀⠀⠀⠈⢣⠀⠀⠀⠀⠠⣤⣀⠀⠀⠀⠀⠀⠙⣄⠀⠀⢚⡟⠯⠟⠀⠀⠀⠀⠀⠉⠈⢿⡀
⠀⠀⢀⣠⠞⠁⠀⠀⠀⣠⠔⠚⠉⠀⢠⠏⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠘⣏⠓⢦⡄⠀⠀⠀⠘⣦⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃
⢀⣴⠟⠁⠀⣀⡀⢀⡴⠋⠀⠀⠀⠀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠹⡆⠀⢻⡆⠀⠀⠀⠸⡆⠀⠙⠢⣄⠀⠀⠀⠀⠀⠀⡼⠁⠀
⣾⣿⠑⣄⡎⠀⣿⠞⠁⠀⠀⠀⠀⢰⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠹⣄⡾⠃⠀⠀⠀⠀⢹⡀⠀⠀⠈⣇⠀⣞⢳⠀⢰⠇⠀⠀
⢻⣿⡀⣸⡿⠋⠁⠀⠀⠀⠀⠀⠈⣿⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠈⢽⣇⠀⠀⠀⠀⠀⢠⣇⠀⠀⠀⠉⢹⠉⢹⠟⠋⠀⠀⠀
⠀⠉⠳⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⠀⠀⠀⠀⠀⠸⡟⠳⡀⡴⠻⣦⡶⣿⠀⠀⠀⣠⠏⠀⢸⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠙⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠟⠁⠀⠀⠀⠀⠀⢳⣼⡟⣿⣆⣾⡶⠋⠀⢀⡴⠋⠀⣀⡾⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠉⣷⠿⠿⠥⠤⠤⠔⠋⠀⢀⡠⡿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠀⠀⠀⠀⠀⠙⢆⡀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣠⠴⢋⡼⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡏⣀⡀⠀⠀⠀⠀⠀⠀⠙⠢⣤⡀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣀⡠⠤⠒⠋⣁⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠹⣄⠁⠀⠀⠀⠀⠀⠀⣠⠖⠋⠉⠑⠒⠒⢺⣄⠀⠀⢀⡀⠀⠀⠀⢸⣇⡀⣀⣠⡤⠖⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⠇⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠹⡄⠀⠀⠈⡇⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣴⡿⣄⣀⠀⠀⠀⠀⣀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠶⠆⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠠⣷⣏⡴⢋⣸⠦⠴⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠛⣧⡴⠋⢳⡀⡞⠹⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠁⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠛⠛⢷⣀⡼⠛⠻⣶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
#draws charmeleon
def draw_charizard():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡜⢛⣤⠀⠀⠀⣀⠜⠛⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠁⣾⠁⢀⣠⠴⠉⢀⣴⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠛⢱⡷⠛⠛⠛⠀⠀⣄⣺⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡰⠋⠉⠀⠀⠀⠀⠀⠀⠀⠸⢇⡀⠀⠀⠀⠀⠀⠀⣰⠶⣂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⣴⠇⣠⠄⠀⢠⣀⢤⣤⠀⠀⠀⢇⠈⢿⣁⠀⠀⠀⠀⠀⠳⢌⡩⢻⣤⣄⣿⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠎⠉⣶⠀⠀⠀⠀⠿⣶⡏⠷⣴⣿⡏⣀⠏⠀⠀⠀⠀⠀⠀⠿⣀⠀⠀⠀⠀⠀⠈⣳⠀⢀⠛⡉⠉⠱⠶⠶⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠙⢀⡸⠀⠀⠀⢀⣀⠬⠛⠑⠃⠀⠀⠀⠀⣠⣤⣤⠄⠀⠀⠀⠘⣿⡀⠀⠀⠀⣀⡀⠀⣿⣁⣦⣿⣿⣿⣿⣤⣤⠀⣻⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⡰⠎⠁⠀⣸⡇⠀⠀⢰⡎⠉⣀⠀⠀⠀⠀⣀⡴⡶⠋⠀⠀⠀⠀⠀⠀⠀⢔⡇⠀⠀⠀⣿⣇⠀⠈⢷⡍⣿⣿⣿⣿⣿⣿⣾⢘⣶⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⠜⠁⢠⣤⣾⣿⡨⣹⠀⠀⠀⢸⡄⠃⠀⣠⡞⣿⢉⣁⣠⣶⣾⣿⡟⠀⠀⠀⠈⠈⢹⡆⠀⢀⡏⢸⡄⠀⢸⣇⣛⣿⣿⣿⣿⣿⣿⡇⠛⡤⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡈⠇⣶⣿⣿⣿⣿⣿⡧⠹⣀⠀⠀⠀⠈⠶⠾⢧⣭⣴⠎⠉⠉⠀⠈⢹⡅⠀⠀⠀⠀⠀⡸⢇⣀⠟⠀⢸⠄⠀⠀⢸⡇⣿⣿⣿⣿⣿⣿⣷⣎⠱⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡇⢨⣿⣿⣿⣿⣿⣿⣿⡇⣿⡀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠄⢸⠂⢀⢸⡇⠀⡀⢸⡏⣴⣿⣿⣿⣿⣿⣿⣿⣿⣤⠸⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠇⢸⣿⣿⣿⣿⣿⣿⣿⣷⣆⣿⣟⠷⠶⢦⣀⣀⡀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢰⠀⠈⣶⠶⢁⣰⠶⢋⣹⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠸⣅⠀⠀⠀
⠀⠀⠀⡾⢠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣥⡙⠓⣤⠀⣀⡤⠤⢚⣻⠇⠀⠀⠀⠸⠀⠀⠀⠛⣤⣚⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠓⡄⠀
⠀⠀⣶⢁⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⡿⠿⠶⣄⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⢱⡆
⠀⢰⠉⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠙⠛⠛⠛⠛⠁⠀⡀⠋⢩⡖⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢂⠀⠈⠉⠉⢻⠛⢻⣿⠟⠛⣿⣿⣿⣿⣿⣿⣿⣿⢸⡇
⢸⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣸⣦⣠⣄⡄⠀⠀⠀⡌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⣴⣶⣶⣦⢀⠈⢱⠀⠀⠀⠈⠉⣿⣿⣿⣿⣒⡎⠁
⠘⢣⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠰⣿⣿⣿⣿⡟⠛⠃⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⠀⠘⢿⣿⣿⡀⠀⣿⠀⠀⠀⠀⣿⣿⣿⡿⣘⡇⠀
⠀⠸⣄⢻⣿⣿⣿⣿⣿⣿⣿⠋⠀⠘⣿⣿⠷⠀⠀⠈⠿⢿⣿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠸⠿⣛⠇⠀⠀⠿⠳⣆⠀⠐⣿⣿⡇⣿⠀⠀
⠀⠀⢿⡎⢹⣿⣿⣿⣿⣿⠏⠀⠀⣸⠋⠁⠀⠀⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢛⡆⠀⣶⠉⠀⡀⠀⠀⢻⡌⣷⠘⢻⡏⣭⠛⠀⠀
⠀⠀⠀⠿⣞⠻⣿⣿⣿⡇⠀⠀⢸⡇⠐⣴⣦⠀⢀⣾⢷⡆⢨⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢱⣾⣇⠒⡎⠉⣿⠒⢺⡷⠋⠀⢸⣧⡿⠀⠀⠀
⠀⠀⠀⠀⢹⡇⠻⣿⣿⣇⠄⠀⠈⠙⣭⠛⢻⡄⣨⠻⡎⠙⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣯⡛⠚⠁⠐⣭⡿⠋⠁⠀⠀⠈⠉⠁⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠷⣘⠻⣿⡏⠀⢄⣀⠀⠀⡰⠎⠉⠉⠀⠀⠀⠀⢆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠼⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠁⠉⢳⣭⣿⡄⠀⠀⣠⡿⠀⠀⠀⠀⠀⠀⠀⠀⢘⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠛⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠼⣀⠀⠀⠒⠤⢄⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡌⠀⠀⠀⢣⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠋⣄⠀⠀⠀⠀⢸⠉⠘⠤⠄⠀⠀⠀⠀⠀⠀⢀⣾⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠅⠠⠤⠤⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⠋⠀⣠⡀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⢢⣼⡇⠀⠀⠀⠀⠀⠀⠀⣲⣽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡴⠆⠀⠀⠀⠻⠃⢸⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⣀⠿⠀⣀⣿⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠶⠾⠉⣶⠀⠀⠀⠀⠀⠀⣘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠟⠉⠀⠀⠀⠉⠀⠀⣿⠍⠉⠑⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠁⠀⠀⠀⣿⠀⠀⠀⢀⣀⡀⠉⣹⡷⣦⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠿⢦⣀⠶⠶⣀⢠⠶⣁⢀⡿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠶⢆⣄⡾⠛⠳⣶⠛⠳⢦⠤⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⠀⣼⣿⠀⣤⣿⣯⡀⡭⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠒⢢⣽⠒⠒⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠘⠋⠀⠀⠘⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
#draws charizard
def train():
    global pokemon_level
    global pokemon_name
    pokemon_level=pokemon_level+1

    gains=(random.randint(1,5))
    if gains==1:
        print(pokemon_name +" found some secret berries and ate some and gained a level. Level is " +str(pokemon_level))
    elif gains==2:
        print(pokemon_name +" did 50 laps and gained a level. Level is now "+str(pokemon_level))
    elif gains==3:
        print(pokemon_name+" broke rocks and gained a level. Level is now "+str(pokemon_level))
    elif gains==4:
        print(pokemon_name+" meditated for an entire day and gained a level. Level is now " +str(pokemon_level))
    elif gains==5:
            print(pokemon_name+ " spent a day in daycare and gained a level. Level is now "+str(pokemon_level))
#"gains" provides extra text while leveling up the pokemon a level
def battle():
    global pokemon_level
    global pokemon_name
    pokemon_level=pokemon_level
    outcome=(random.randint(1,4))
    print("Would you like to battle: Yes or No?")
    input("Select yes or no")
    if outcome==1 and pokemon_level<=20:
        print("Your " +pokemon_name+" prevailed and won the battle. Level increased to "+str(pokemon_level+2))
#Because the pokemon is not a high level, they have less chances to win a pokemon battle
    elif outcome==1 and pokemon_level>=20:
        print("Your "+pokemon_name+" swiftly defeated the opponent. Their level is now "+str(pokemon_level+2))
    elif outcome==2 and pokemon_level>=20:
        print("Your "+pokemon_name+" successfully defeated their opponent. Their level is now "+str(pokemon_level+2))
    elif outcome==3 and pokemon_level>=20:
        print("Your "+pokemon_name+" blitzed their opponent in record time. They are now "+str(pokemon_level+2))
#Once a pokemon is past 20, they can win more easily
    else:
        print("Your " +pokemon_name+" was defeated and cannot go on.")
#if the pokemon is not past level 20 or hits the option 4, they "lose" the battle and don't gain a level
    if pokemon_level<=15:
        print("Sorry but "+pokemon_name+" is unable to battle due to low level. Train them up to be able to battle")
    elif pokemon_level>=15:
        print("Congrats your pokemon is eligible to battle.")
        print("Would you like to battle: Yes or No?")
        input("Select yes or no")
    #Decides if the pokemon can battle or needs to level up
#lets user battle pokemon for levels








def evolve():
    global pokemon_name
    global pokemon_level
    if pokemon_level==20 or pokemon_level>=20:
        print("Congrats your Charmander has now evolved to Charmeleon")
        pokemon_name="Charmeleon"
    if pokemon_level==30:
        print("Amazing your Charmeleon evolved into a Charizard")
        pokemon_name="Charizard"
##This function enables pokemon to change "forms" by changing their name after a certain level
def display():
    global pokemon_name
    global pokemon_level
    print(pokemon_name)
    print(str(pokemon_level))
    if pokemon_level>=0:
        draw_charmander()
    if pokemon_level>=20:
        draw_charmeleon()
    if pokemon_level>=30:
        draw_charizard()
#shows the user the pokemon and displays its name and level
def pokemon():
    print("Welcome to Pokemon Evolution")
while True:
    print("Choose an activity for Day: "+str(day))
    print("""1. Train
2.Gym Battle
3. Rest(Display info)
4.quit
""")
    activity=int(input("Activity for the day: "))




    if activity==1:
        train()
        evolve()
    if  activity==2:
        battle()
        evolve()
    if activity==3:
        display()
    if activity==4:
        print("Thanks for playing!")
        break






    day=day+1
#the whole game of Pokemon
#Main
pokemon()

