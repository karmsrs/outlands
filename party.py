from os import path, _exit, listdir
from time import sleep

class UOPartyJournal:
    JOURNAL_PATH = 'C:\\Program Files (x86)\\Ultima Online Outlands\\ClassicUO\\Data\\Client\\JournalLogs'

    def __init__(self):
        self.lastJournalPath = None
        self.curJournalPath = None

    def getLogPath(self):
        _latestPath = path.join(self.JOURNAL_PATH, sorted(listdir(self.JOURNAL_PATH))[-1])
        if self.curJournalPath == _latestPath:
            return False
        else:
            self.lastJournalPath = self.curJournalPath
            self.curJournalPath = _latestPath
            return True

    def followFile(self, journalFile):
        try:
            while True:
                line = journalFile.readline()
                if self.getLogPath():
                    break
                elif not line or not line.endswith('\n'):
                    sleep(0.1)
                    continue
                elif not '[Party]' in line:
                    continue
                yield line
        except KeyboardInterrupt:
            _exit(1)

    def journal(self):
        while True:
            self.getLogPath()
            journalFile = open(self.curJournalPath, 'r')
            journalLines = self.followFile(journalFile)
            for line in journalLines:
                print(line.split('  ', 1)[1], end='')

if __name__ == '__main__':
    journal = UOPartyJournal()
    journal.journal()