er1 = int(input("your prompt:  "))
match er1:
  case 0:
    print("default")

  case 1:
    print("you chose 1")
  case _ if er1 > 10:
    print("high")
  case 7:
    print("lucky")
  case 100:
    print("santuary")
