VSCODE 中设置Python环境变量,设置完成后需要重启。
Code->Preference->Setting->terminal.integrated.env.osx
或者：
 terminal.integrated.env.windows / terminal.integrated.env.linux / terminal.integrated.env.osx 

 ```
 {
    "terminal.integrated.env.windows": {
        "ENVIRON_VARIABLE": "The Variable value",
        "VAR2": "111",
        // 下面没加引号的是错的，不会生效
        //"VAR3": 111,
    },
}
 ```
 重启不要忘记了