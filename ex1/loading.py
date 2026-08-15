import importlib


def check_depedencies() -> tuple[dict, bool]:
    print("Checking dependencies:")
    deps = [("pandas", "Data manipulation ready"),
            ("numpy", "Numerical computation ready"),
            ("matplotlib", "Visualization ready")]
    mods = {}
    for dep, dep_des in deps:
        try:
            mods[dep] = importlib.import_module(dep)
            print(f"[OK] {dep} ({mods[dep].__version__}) - {dep_des}")
        except Exception as e:
            print(e)
            print(f"[Missing] {dep} depedency")
            print(f"install with pip: pip install {dep}")
            print(f"or install with poetry: poetry add {dep}")
    if len(deps) != len(mods):
        print("Install all required depedencies:")
        print("Install with pip: pip install -r requirements.txt")
        print("Install with poetry: poetry install")
        return {}, False
    return mods, True


def analyze_matrix(mods: dict) -> None:
    print("Analyzing Matrix data...")

    pd = mods['pandas']
    np = mods['numpy']
    try:
        plt = importlib.import_module('matplotlib.pyplot')
    except Exception as e:
        print(e)
        return

    print('Processing 1000 data points...')
    x = np.round(np.linspace(0, 4 * np.pi, 1000), 5)
    y = np.round(np.cos(x), 5)
    z = np.round(np.sin(x), 5)
    df = pd.DataFrame({'Time': x, 'Signal y': y, 'Signal z': z})
    print(df.describe().round(5))

    print('Generating visualization...')
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(df['Time'], df['Signal y'], df['Signal z'])
    plt.grid(True)
    ax.set_xlabel('Time')
    ax.set_ylabel('Signal')
    ax.set_zlabel('Signal')
    plt.title('Signal against Time graph')
    plt.savefig('matrix_analysis')
    plt.close()
    print()

    print('Analysis complete!')
    print('Results saved to: matrix_analysis.png')


def compare_versions(mods: dict) -> None:
    print("Package Version Comparison (pip vs Poetry):")
    for name, mod in mods.items():
        version = getattr(mod, "__version__", "unknown")
        print(f"  {name:<12} {version}")
    print()
    print(
        "pip:    requirements.txt pins exact versions (==) via 'pip freeze',"
    )
    print(
        "          covering every installed package, direct and transitive."
    )
    print(
        "  Poetry: pyproject.toml declares flexible ranges (>=x,<y) for direct"
    )
    print(
        "          dependencies; poetry.lock pins the full resolved tree."
    )
    print()


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()

    mods, result = check_depedencies()
    print()

    if result:
        analyze_matrix(mods)
    print()

    compare_versions(mods)


if __name__ == "__main__":
    main()
