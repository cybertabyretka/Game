from shelve import open as open_sh


class Save:
    def __init__(self, file_path):
        with open_sh(file_path) as save_file:
            if 'game' not in save_file.keys():
                save_file['game'] = None
            if 'date' not in save_file.keys():
                save_file['date'] = '--.--.---- --;--;--'
                self.date = '--.--.---- --;--;--'
            else:
                self.date = save_file['date']