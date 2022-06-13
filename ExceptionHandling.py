def basicException():
    try:
        return 42/0
    except ZeroDivisionError as e:
        print("Error : {}".format(e))
    except Exception as e:
        print("Error : {}".format(e))
    finally:
        print("Excecution completed")

basicException()