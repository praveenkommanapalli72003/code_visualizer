from flask import Flask, render_template, request, jsonify
import ast, subprocess, tempfile, os

app = Flask(__name__)

# ---------------- PYTHON VISUALIZER ----------------
def python_engine(code):
    steps = []
    variables = {}
    output = []
    step = 1

    tree = ast.parse(code)

    for node in tree.body:

        # Assignment
        if isinstance(node, ast.Assign):
            var = node.targets[0].id
            val = eval(compile(ast.Expression(node.value), "", "eval"), {}, variables)
            variables[var] = val
            steps.append({
                "step": step,
                "line": f"{var} = {val}",
                "variables": variables.copy(),
                "output": output.copy()
            })
            step += 1

        # For loop
        elif isinstance(node, ast.For):
            loop_var = node.target.id
            loop_range = eval(compile(ast.Expression(node.iter), "", "eval"), {}, variables)

            for i in loop_range:
                variables[loop_var] = i
                steps.append({
                    "step": step,
                    "line": f"{loop_var} = {i}",
                    "variables": variables.copy(),
                    "output": output.copy()
                })
                step += 1

                for body in node.body:
                    # Assignment inside loop
                    if isinstance(body, ast.Assign):
                        var = body.targets[0].id
                        val = eval(
                            compile(ast.Expression(body.value), "", "eval"),
                            {},
                            variables
                        )
                        variables[var] = val
                        steps.append({
                            "step": step,
                            "line": f"{var} = {val}",
                            "variables": variables.copy(),
                            "output": output.copy()
                        })
                        step += 1

                    # print()
                    elif isinstance(body, ast.Expr) and isinstance(body.value, ast.Call):
                        if body.value.func.id == "print":
                            val = eval(
                                compile(ast.Expression(body.value.args[0]), "", "eval"),
                                {},
                                variables
                            )
                            output.append(str(val))
                            steps.append({
                                "step": step,
                                "line": f"print({val})",
                                "variables": variables.copy(),
                                "output": output.copy()
                            })
                            step += 1

    return {"type": "visualizer", "steps": steps}

# ---------------- C++ EXECUTOR ----------------
def cpp_engine(code):
    with tempfile.TemporaryDirectory() as d:
        cpp_file = os.path.join(d, "main.cpp")
        exe_file = os.path.join(d, "a.out")

        with open(cpp_file, "w") as f:
            f.write(code)

        compile = subprocess.run(
            ["g++", cpp_file, "-o", exe_file],
            capture_output=True, text=True
        )
        if compile.returncode != 0:
            return {"type": "output", "output": compile.stderr}

        run = subprocess.run([exe_file], capture_output=True, text=True)
        return {"type": "output", "output": run.stdout}

# ---------------- JAVA EXECUTOR ----------------
def java_engine(code):
    with tempfile.TemporaryDirectory() as d:
        java_file = os.path.join(d, "Main.java")

        with open(java_file, "w") as f:
            f.write(code)

        compile = subprocess.run(
            ["javac", "Main.java"],
            cwd=d, capture_output=True, text=True
        )
        if compile.returncode != 0:
            return {"type": "output", "output": compile.stderr}

        run = subprocess.run(
            ["java", "Main"],
            cwd=d, capture_output=True, text=True
        )
        return {"type": "output", "output": run.stdout}

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run():
    data = request.json
    code = data["code"]
    lang = data["language"]

    if lang == "python":
        return jsonify(python_engine(code))
    elif lang == "cpp":
        return jsonify(cpp_engine(code))
    elif lang == "java":
        return jsonify(java_engine(code))

    return jsonify({"error": "Unsupported language"})

if __name__ == "__main__":
    app.run(debug=True, port=8000)




