#/bin/sh
if [ ! -d "~/.local/share/fcitx5/rime" ]; then
    cp -f *.yaml ~/.local/share/fcitx5/rime
elif [ ! -d "~/.local/share/fcitx/rime" ]; then
    cp -f *.yaml ~/.local/share/fcitx/rime
elif [ ! -d "~/.config/ibus/rime" ]; then
    cp -f *.yaml ~/.config/ibus/rime
else
    echo "Your RIME installation not found."
    echo "Mmeh zinjiak nikeh RIME oetzong weicy."
fi
