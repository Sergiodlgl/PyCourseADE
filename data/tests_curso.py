def test_calcular_roi(fun):
    assert abs(fun(1000, 1200) - 0.2) < 0.0001, "Error en test 1"
    assert abs(fun(500, 750) - 0.5) < 0.0001, "Error en test 2"
    assert abs(fun(2000, 1800) + 0.1) < 0.0001, "Error en test 3"
    print("✅ Todos los tests de ROI pasaron.")

def test_calcular_clv(fun):
    assert fun([(1000, 400), (1200, 500), (1500, 700)]) == 3100 - 1600, "Error en test 1"
    assert fun([(500, 100), (600, 100)]) == 1000, "Error en test 2"
    assert fun([]) == 0, "Error en test 3 (lista vacía)"
    assert fun([(100, 150)]) == -50, "Error en test 4 (CLV negativo)"
    print("✅ Todos los tests de CLV pasaron.")
