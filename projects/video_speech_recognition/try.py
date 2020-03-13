try:
    from SimpleAudioIndexer import SimpleAudioIndexer as sai
    indexer = sai(mode="ibm", src_dir=" D:\python\projects\video_speech_recognition\recording.wav",
                username_ibm="abubakark1998@gmail.com", password_ibm="Losogen1i")
    indexer.index_audio()
    searcher = indexer.search_gen(query="called")
    # If you're on python 2.7, instead of below, do print searcher.next()
    print(next(searcher))
    # {'Query': 'called', 'File Name': 'small_audio.wav', 'Result': (1.25, 1.71)}
    print(indexer.search_regexp(pattern="[A-Z][^l]* ")
except Exception as ex:
    print(ex.__class__.__name__ + " : " + ex.__str__())
