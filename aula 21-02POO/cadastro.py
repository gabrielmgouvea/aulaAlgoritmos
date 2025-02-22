import banco

ze = banco.Banco("Saqua Eng Software", 1, 1, "Zé da Manga", "123456123789")

zecove = banco.Banco("Inter", 1, 1000, "Zé das Coves", "000019237812")

print(ze)

print(zecove)

zecove.definir_senha(12345)
ze.definir_senha("admin01")

ze.deposito(5000)

ze.pix(zecove, 2000)

ze.saque("admin01", 1000)

ze.extrato()

zecove.extrato()
