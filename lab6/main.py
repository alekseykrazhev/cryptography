# cryptography lab 6 Elgamal and SHA-2 implementation

from Elgamal import generate_key, sign, verify


if __name__ == '__main__':
    # 70632854428090245668612719837589154263674140045063326147121864128289640672721
    q = 70632854428090245668612719837589154263674140045063326147121864128289640672721

    # Elgamal
    # keypair: 0 - p, 1 - q, 2 - g, 3 - e, 4 - d
    keypair = generate_key(q)

    print(f"CP params: {keypair[0]} {keypair[1]} {keypair[2]}")
    print(f"Public key: {keypair[3]}")
    print(f"Private key: {keypair[4]}")

    sign_msg = sign(keypair[0], keypair[1], keypair[2], keypair[4], 'Im Aleksey Krazhevskiy, and I love CM!')
    print(f"Signature: {sign_msg}")

    verify_msg = verify(keypair[0], keypair[1], keypair[2], keypair[3], 'Im Aleksey Krazhevskiy, and I love CM!',
                        sign_msg[0], sign_msg[1])
    print(f"Verify: {verify_msg}")
