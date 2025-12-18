chai_menu={"masala chai":50,"ginger chai":60,"cardamom chai":70,"tulsi chai":80}

# chai_menu["lemon chai"]  # this will give KeyError

try:
    chai_menu["lemon chai"]
except KeyError:
    print("Lemon chai is not available")




print("hello chai code")