import os

def main():
  command = "apt install nc"
  command2 = "apt install netcat"

  try:
    os.ystem(command)
  except Exception as e:
    os.system(command2)

  command3 = "nc -lvnp 4444"
  try:
    os.system(command3)
  except Exception as e:
    print(f"Error al ponerse en escucha: {e}")

if __name__ == '__main__':
  main()
