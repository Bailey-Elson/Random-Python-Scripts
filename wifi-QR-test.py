# pip install qrcode[pil]
import qrcode

# wifi_info variable is the netword info
# Repalce Wifi-Name with the Network NAme
# Repalce Password123 with the Network Password
wifi_info = "WIFI:T:WPA;S:Wifi-Name;P:Password123;;"
img = qrcode.make(wifi_info)
img.save("wifi_qr.png")

print("QR code saved as wifi_qr.png")

