import os


class GenerateFen:
    def __init__(self, directory):
        self.directory = directory
        self.pgn_list = []


    def readPGNFile(self):
        for fileName in os.listdir(self.directory):
            filePath = os.path.join(self.directory, fileName)
            pgn_found = False
            if os.path.isfile(filePath):
                with open(filePath) as pgn_file:
                    pgn = ""
                    lines = pgn_file.readlines()
                    for line in lines:
                        if not line.strip():
                            if pgn_found:
                                self.pgn_list.append(pgn.strip())
                                pgn = ""
                            pgn_found = not pgn_found
                            continue
                        if pgn_found:
                            pgn += ' ' + line.strip()
                        else:
                            continue
                    self.pgn_list.append(pgn.strip())

