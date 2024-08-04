import numpy as np

def calculate_mac(phi_a, phi_b):
    phi_a_norm = phi_a / np.linalg.norm(phi_a)
    phi_b_norm = phi_b / np.linalg.norm(phi_b)
    mac = np.abs(phi_a_norm @ phi_b_norm)**2
    return mac

phi_a = np.array([1, 2, 3])
phi_b = np.array([1, 2, 2.9])

mac_value = calculate_mac(phi_a, phi_b)
print(f'MAC value: {mac_value}')
