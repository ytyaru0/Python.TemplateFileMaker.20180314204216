try:
    raise Exception('例外発生')
except Exception as e:
    print(e)
    print('例外キャッチ')
finally:
    print('例外終了')
