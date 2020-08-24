# Jupyter NoteBook Keyboard sortcuts快捷键

The Jupyter Notebook has two different keyboard input modes. 

**Edit mode** allows you to type code or text into a cell and is indicated by a green cell border. 

**Command mode** binds the keyboard to noteb
ook level commands and is indicated by a grey cell border with a blue left margin.

### 命令模式快捷键- Esc 键开启-Command Mode (press Esc to enable):

| 快捷键       | 作用                         | 说明                                                         |
| ------------ | ---------------------------- | ------------------------------------------------------------ |
| Enter        | 转入编辑模式                 | Enter: enter edit mode                                       |
| Shift-Enter  | 运行本单元，选中下个单元     | 新单元默认为命令模式 Shift-Enter: run cell, select below     |
| Ctrl-Enter   | 运行本单元                   | Ctrl-Enter: run selected cells                               |
| Alt-Enter    | 运行本单元，在其下插入新单元 | 新单元默认为编辑模式Alt-Enter: run cell and insert below     |
| Y            | 单元转入代码状态             | Y: change cell to code                                       |
| M            | 单元转入 markdown 状态       | M: change cell to markdown                                   |
| R            | 单元转入 raw 状态            | R: change cell to raw                                        |
| 1            | 设定 1 级标题                | 仅在 markdown 状态下时建议使用标题相关快捷键，如果单元处于其他状态，则会强制切换到 markdown 状态1: change cell to heading 1 |
| 2            | 设定 2 级标题                | 2: change cell to heading 2                                  |
| 3            | 设定 3 级标题                | 3: change cell to heading 3                                  |
| 4            | 设定 4 级标题                | 4: change cell to heading 4                                  |
| 5            | 设定 5 级标题                | 5: change cell to heading 5                                  |
| 6            | 设定 6 级标题                | 6: change cell to heading 6                                  |
| Up           | 选中上方单元                 | K: select cell above                                         |
| K            | 选中上方单元                 | Up: select cell above                                        |
| Down         | 选中下方单元                 | Down: select cell below                                      |
| J            | 选中下方单元                 | J: select cell below                                         |
| Shift-K      | 连续选择上方单元             | Shift-K: extend selected cells above                         |
| Shift-J      | 连续选择下方单元             | Shift-J: extend selected cells below                         |
| Shift-Up     | 连续选择上方单元             | Shift-Up: extend selected cells above                        |
| Shift-Down   | 连续选择下方单元             | Shift-Down: extend selected cells below                      |
| A            | 在上方插入新单元             | A: insert cell above                                         |
| B            | 在下方插入新单元             | B: insert cell below                                         |
| Alt-F        | 代码折叠                     | Alt-F: Toggle codefolding                                    |
| X            | 剪切选中的单元               | X: cut selected cells                                        |
| C            | 复制选中的单元               | C: copy selected cells                                       |
| Shift-V      | 粘贴到上方单元               | Shift-V: paste cells above                                   |
| V            | 粘贴到下方单元               | V: paste cells below                                         |
| Z            | 恢复删除的最后一个单元       | Z: undo cell deletion                                        |
| D,D          | 删除选中的单元               | 连续按两个 D 键 D,D: delete selected cells                   |
| Shift-M      | 合并选中的单元               | Shift-M: merge selected cells, or current cell with cell below if only one cell is selected |
| Ctrl-S       | 保存当前 NoteBook            | Ctrl-S: Save and Checkpoint                                  |
| S            | 保存当前 NoteBook            | S: Save and Checkpoint                                       |
| L            | 开关行号                     | 编辑框的行号是可以开启和关闭的L: toggle line numbers         |
| O            | 转换输出                     | O: toggle output of selected cells                           |
| Shift-O      | 转换输出滚动                 | Shift-O: toggle output scrolling of selected cells           |
| Esc          | 关闭页面                     | Esc: close the pager                                         |
| Ctrl-L       | 格式化选定单元格代码         | Ctrl-L: code_prettify selected cell(s)                       |
| Ctrl-Shift-L | 格式化整个笔记代码           | Ctrl-Shift-L: code_prettify the whole notebook               |
| P            | 打开命令行                   | P: open the command palette                                  |
| Q            | 关闭页面                     | Q: close the pager                                           |
| H            | 显示快捷键帮助               | H: show keyboard shortcuts                                   |
| F            | 查找替换                     | F: find and replace                                          |
| Ctrl-Shift-F | 打开命令行                   | Ctrl-Shift-F: open the command palette                       |
| Ctrl-Shift-P | 打开命令行                   | Ctrl-Shift-P: open the command palette                       |
| I,I          | 中断 NoteBook 内核           | I,I: interrupt the kernel                                    |
| 0,0          | 重启 NoteBook 内核           | 0,0: restart the kernel (with dialog)                        |
| Shift-L      | 行号显示                     | Shift-L: toggles line numbers in all cells, and persist the setting |
| Shift        | 忽略                         |                                                              |
| Shift-Space  | 向上滚动                     | Shift-Space: scroll notebook up                              |
| Space        | 向下滚动                     | Space: scroll notebook down                                  |

### 编辑模式快捷键- 按 Enter 键启动-Edit Mode (press Enter to enable):

| 快捷键         | 作用                         | 说明                                                         |
| -------------- | ---------------------------- | ------------------------------------------------------------ |
| Tab            | 代码补全或缩进               | Tab: code completion or indent                               |
| Shift-Tab      | 提示                         | 输出帮助信息，部分函数、类、方法等会显示其定义原型，如果在其后加 `?` 再运行会显示更加详细的帮助 Shift-Tab: tooltip |
| Ctrl-]         | 缩进                         | 向右缩进 Ctrl-]: indent                                      |
| Ctrl-[         | 解除缩进                     | 向左缩进 Ctrl-[: dedent                                      |
| Ctrl-A         | 全选                         | Ctrl-A: select all                                           |
| Ctrl-Z         | 撤销                         | Ctrl-Z: undo                                                 |
| Ctrl-Shift-Z   | 重做                         |                                                              |
| Ctrl-D         | 删除整行                     | Ctrl-D: delete whole line                                    |
| Ctrl-Y         | 重做                         | Ctrl-Y: redo                                                 |
| Ctrl-U         | 撤销选择                     | Ctrl-U: undo selection                                       |
| Ctrl-Home      | 跳到单元开头                 | Ctrl-Home: go to cell start                                  |
| Ctrl-Up        | 跳到单元开头                 | Ctrl-Up: go to cell start                                    |
| Ctrl-End       | 跳到单元末尾                 | Ctrl-End: go to cell end                                     |
| Ctrl-Down      | 跳到单元末尾                 | Ctrl-Down: go to cell end                                    |
| Ctrl-Left      | 跳到左边一个字首             | Ctrl-Left: go one word left                                  |
| Ctrl-Right     | 跳到右边一个字首             | Ctrl-Right: go one word right                                |
| Ctrl-Backspace | 删除前面一个字               | Ctrl-Backspace: delete word before                           |
| Ctrl-Delete    | 删除后面一个字               | Ctrl-Delete: delete word after                               |
| Esc            | 切换到命令模式               | Esc: enter command mode                                      |
| Ctrl-M         | 切换到命令模式               | Ctrl-M: enter command mode                                   |
| Shift-Enter    | 运行本单元，选中下一单元     | 新单元默认为命令模式，Shift-Enter: run cell, select below    |
| Ctrl-Enter     | 运行本单元                   | Ctrl-Enter: run selected cells                               |
| Alt-Enter      | 运行本单元，在下面插入一单元 | 新单元默认为编辑模式Alt-Enter: run cell and insert below     |
| Ctrl-Shift–    | 分割单元                     | 按光标所在行进行分割，Ctrl-Shift-Minus: split cell at cursor |
| Alt-U          | 重新选择                     | Alt-U: redo selection                                        |
| Ctrl-Shift-F   | 打开命令行                   | Ctrl-Shift-F: open the command palette                       |
| Ctrl-Shift-P   | 打开命令行                   | Ctrl-Shift-P：open the command palette                       |
| Alt-C          | 注释                         | Alt-C: Toggle comments                                       |
| Alt-F          | 代码折叠                     | Alt-F: Toggle codefolding                                    |
| Ctrl-S         | 保存当前 NoteBook            | Ctrl-S: Save and Checkpoint                                  |
| Shift          | 忽略                         |                                                              |
| Up             | 光标上移或转入上一单元       | Up: move cursor up                                           |
| Down           | 光标下移或转入下一单元       | Down: move cursor down                                       |
| Ctrl-/         | 注释整行/撤销注释            | 仅代码状态有效, Ctrl-/: comment                              |
| Ctrl-Shift-L   | 格式化文档                   | Ctrl-Shift-L: code_prettify the whole notebook               |
| Ctrl-L         | 格式化选定单元格代码         | Ctrl-L: code_prettify selected cell(s)                       |
| Insert         | Insert                       | Insert: toggle overwrite flag                                |