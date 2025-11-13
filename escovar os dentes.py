print("olá usuário, vamos escovar os dentes:")
print("pegue a escova,")
print("agora coloque a pasta na escova.")
decisão=input("digite 'terminei' ao terminar de escovar os dentes:")
if decisão.lower() == "terminei":
 decisão=input("Você escovou bem todos os dentes? (sim/não): ")
if decisão.lower() == "sim":
    print("Agora enxágue bem a boca e guarde a escova.")
    print("E está pronto! Dentes escovados.")
else:
    print("Então continue escovando os dentes até terminar, e escove bem.")
