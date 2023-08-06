from cs200.main import Controller

def main():
    ctrl = Controller()
    ctrl.init_args()
    ctrl.write_summarization()

def install():
    import nltk
    nltk.download("punkt")
