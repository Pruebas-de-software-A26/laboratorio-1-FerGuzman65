import user_manager
import logging

logging.basicConfig(

 level= logging.DEBUG,
 filename= "",
 filemode="w"
 )





if __name__== "__main__":
    manager=user_manager.UserManager()
    logging.info("test case 1(RF1)")
    manager.add_user(1, "Alice")
    logging.info("PASS using the debugger")
    logging.info("end test case")
    logging.info("test case 2(RF2)")

    manager.add_user(2, "Bob")
    manager.add_user(3, "Charlie")


    user1=manager.find_user(1)

    logging.info("before if")
if user1["name"]  =="Alice":
    logging.info("PASS")
else:
    logging.info("FAIL")


logging.info("test case 3")
manager.delete_user(2)
logging.info("test case PASS using the debugger")
all_names=manager.get_all_names()
logging.info(f"all names: {all_names}")

if all_names==["Alice", "Charlie"]:
    logging.info("PASS")
else:
    logging.error("FAIL")
    logging.warning(" the function retuns the IDs:")




logging.info("test case 5(RNF1)")
for i in range (1000):
    manager.add_user(i,"User"+str(i))
    logging.info(f"added user {i}")




logging.info(manager.find_user(500))