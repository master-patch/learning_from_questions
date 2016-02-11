rm minecraft_text_concat.raw;
rm minecraft_text_concat.parsed;

cat minecraft_text.raw noisy_minecraft_text.raw >> minecraft_text_concat.raw
cat minecraft_text.parsed noisy_minecraft_text.parsed >> minecraft_text_concat.parsed
