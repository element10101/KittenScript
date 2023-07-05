from sys import stderr

variables = {}
constants = {}

with open("main.kts") as kts:
  kts = kts.read()
  for ksl in kts:
    if ksl.startswith("let"):
      """
      Create a variable.

      Syntax: `let <variable> of type <type> be <value>`
      """
      kslp = ksl.split()
      name = kslp[1]
      typ = kslp[4]
      value = kslp[6]
      if name in variables or name in constants:
        stderr.write(f"""Error code: NO_RECREATING_CATS<{name}>""")
        break
      if typ == "int":
        value = int(value)
      elif typ == "float":
        value = float(value)
      elif typ == "string":
        value = str(value)
      else:
        stderr.write(f"""Error code: INVALID_SHELTER<{typ}>""")
        break
      variables[name] = value
      continue
    elif ksl.startswith("const"):
      """
      Create a constant variable.

      Syntax: `const <variable> of type <type> is <value>`
      """
      kslp = ksl.split()
      name = kslp[1]
      typ = kslp[4]
      value = kslp[6]
      if name in variables or name in constants:
        stderr.write(f"""Error code: NO_RECREATING_CATS<{name}>""")
        break
      if value == "!var":
        varval = kslp[7]
        if varval in variables:
          value = variables[varval]
        elif varval in constants:
          value = variables[varval]
        else:
          stderr.write(f"""Error code: LOST_CAT<{varval}>""")
          break
      else:
        if typ == "int":
          value = int(value)
        elif typ == "float":
          value = float(value)
        elif typ == "string":
          value = str(value)
      constants[name] = value
      continue
    elif ksl.startswith("set"):
      """
      Set an existing variable to a new value.

      Syntax: `set <variable> to <value> with type <type>`
      """
      kslp = ksl.split()
      name = kslp[1]
      value = kslp[3]
      typ = kslp[6]
      if name in constants:
        stderr.write(f"""Error code: UNMODIFIABLE_LION<{name}>""")
        break
      elif name in variables:
        if typ == "int":
          value = int(value)
        elif typ == "float":
          value = float(value)
        elif typ == "string":
          value = str(value)
        else:
          stderr.write(f"""Error code: INVALID_SHELTER<{typ}>""")
          break
        variables[name] = value
      else:
        stderr.write(f"""Error code: LOST_CAT<{varval}>""")
        break
      continue
    elif ksl.startswith("print"):
      """
      Print text to the console.

      Syntax: `print <text>`
      """
      printed = ksl[6:-1] + ksl[-1]
      if printed.startswith("!var"):
        var = printed.split()[1]
        if var in variables:
          print(str(variables[var]))
        elif var in constants:
          print(str(constants[var]))
        else:
          stderr.write(f"""Error code: LOST_CAT<{var}>""")
          break
      else:
        print(printed.replace("!new!", "\n"))
      continue
