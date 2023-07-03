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
      type = kslp[4]
      value = kslp[6]
      if type == "int":
        value = int(value)
      elif type == "float":
        value = float(value)
      elif type == "str":
        value = str(value)
      variables[name] = value
      continue
    elif ksl.startswith("const"):
      """
      Create a constant variable.

      Syntax: `const <variable> of type <type> is <value>`
      """
      kslp = ksl.split()
      name = kslp[1]
      type = kslp[4]
      value = kslp[6]
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
        if type == "int":
          value = int(value)
        elif type == "float":
          value = float(value)
        elif type == "str":
          value = str(value)
      constants[name] = value
    elif ksl.startswith("set"):
      """
      Set an existing variable to a new value.

      Syntax: `set <variable> to <value> with type <type>`
      """
      kslp = ksl.split()
      name = kslp[1]
      value = kslp[3]
      type = kslp[6]
      if name in constants:
        stderr.write(f"""Error code: UNMODIFIABLE_LION<{name}>""")
        break
      elif name in variables:
        pass
      else:
        stderr.write(f"""Error code: LOST_CAT<{varval}>""")
