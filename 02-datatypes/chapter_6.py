chai_type="Ginger chai"

#encoding
label_text="atharva"
encoded_label=label_text.encode("utf-8")
print(f"Non-encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label=encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")