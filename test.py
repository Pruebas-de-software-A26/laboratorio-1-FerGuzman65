import logging
import user_manager
import time

logging.basicConfig(
    level=logging.DEBUG,
    filemode="w",
    filename="TEST.log"
)

if __name__ == "__main__":
    manager = user_manager.UserManager()

    # caso 1 (RF1)
    manager.add_user(1, "Alice")

    # caso 2 (RF2)
    manager.add_user(2, "Bob")
    manager.add_user(3, "Charlie")
    user1 = manager.find_user(1)
    if user1["name"] == "Alice":
        logging.info("PASS")
    else:
        logging.info("FAIL")

    # caso 3 (RF3)
    manager.delete_user(2)
    all_names = manager.get_all_names()
    logging.info(f"all names: {all_names}")
    if all_names == ["Alice", "Charlie"]:
        logging.info("PASS")
    else:
        logging.error("FAIL")

    # caso 4 (RF4/RF5)
    names = manager.get_all_names()
    logging.info(f"all names: {names}")
    avg_id = manager.average_user_id()
    logging.info(f"average user id: {avg_id}")

    # caso 5 (RNF1/RNF2)
    for i in range(1000):
        manager.add_user(i, "User" + str(i))
    inicio=time.perf_counter()
    resultado=manager.find_user(500)
    fin=time.perf_counter()
    duracion_total=fin-inicio
    logging.info(f"tiempo total {duracion_total}, usuario{resultado}")


    # caso 6 (robustez)
    
    antes=manager.get_all_names()
    idd=manager.delete_user(100000)
    despues=manager.get_all_names()
    if antes==despues:
        logging.warning(f"Usuario no encontrado:{idd}")
    else:
        logging.info(f"Usuario eliminado{idd}")


    vacio=user_manager.UserManager()
    try:
        respuesta=vacio.average_user_id()
        logging.info(f"Resultado{respuesta}")
    except ZeroDivisionError:
        logging.error(f"FAIL")    
    # caso 7 (duplicados)

    manager.add_user(3,"duplicado")
    duplicado=manager.find_user(3)
    buscador=sum(1 for u in manager.users if u["id"]==3)
    logging.info(f"usuarios con id 3: {buscador}")
    if buscador == 1:
        logging.info("Ya habia uno")
    else:
        logging.error("ya habia uno con ese nombre")
