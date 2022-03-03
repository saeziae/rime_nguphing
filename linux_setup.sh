#/bin/sh
if [ ! -d "~/.local/share/fcitx5/rime" ]; then
    cp -f *.yaml ~/.local/share/fcitx5/rime
    grep <~/.local/share/fcitx5/rime/default.yaml >/dev/null nguphing || vim ~/.local/share/fcitx5/rime/default.yaml
elif [ ! -d "~/.local/share/fcitx/rime" ]; then
    cp -f *.yaml ~/.local/share/fcitx/rime
    grep <~/.local/share/fcitx/rime/default.yaml >/dev/null nguphing || vim ~/.local/share/fcitx/rime/default.yaml
elif [ ! -d "~/.config/ibus/rime" ]; then
    cp -f *.yaml ~/.config/ibus/rime
    grep <~/.config/ibus/rime/default.yaml >/dev/null nguphing || vim ~/.config/ibus/rime/default.yaml
else
    echo "Your RIME installation not found."
    echo "Mmeh zinjiak nikeh RIME oetzong weicy."
fi
