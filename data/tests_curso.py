def test_calcular_roi(fun):
    assert abs(fun(1000, 1200) - 0.2) < 0.0001, "Error en test 1"
    assert abs(fun(500, 750) - 0.5) < 0.0001, "Error en test 2"
    assert abs(fun(2000, 1800) + 0.1) < 0.0001, "Error en test 3"
    print("✅ Todos los tests de ROI pasaron.")
