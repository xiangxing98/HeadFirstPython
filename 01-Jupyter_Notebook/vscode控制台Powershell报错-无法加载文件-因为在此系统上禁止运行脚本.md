# vscode控制台Powershell报错-无法加载文件-因为在此系统上禁止运行脚本

> 使用vscode自带集成终端Powershell报错解决方案
>
> 参考：https://blog.csdn.net/larpland/article/details/101349586?utm_medium=distribute.pc_relevant.none-task-blog-title-1&spm=1001.2101.3001.4242

## 现象

打开控制台方式，选项View -> Terminal，控制台Powershell报错

```
. : 无法加载文件 C:\Users\xiang\Documents\WindowsPowerShell\profile.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参阅 https:/go.microsoft.com/fwlink/?Lin
kID=135170 中的 about_Execution_Policies。
所在位置 行:1 字符: 3
+ . 'C:\Users\xiang\Documents\WindowsPowerShell\profile.ps1'
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) []，PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
加载个人及系统配置文件用了 725 毫秒。
```

## 命令行解决报错：

（1）以管理员身份运行vs code

（2）查询Powershell详细策略，在终端执行：get-ExecutionPolicy，显示Restricted（禁止状态）

```
PS F:\Github\Python\HeadFirstPython\HeadFirstPython> Get-ExecutionPolicy  
Restricted
```

（3）更新Powershell策略，在终端执行：set-ExecutionPolicy RemoteSigned

```
PS F:\Github\Python\HeadFirstPython\HeadFirstPython> Set-ExecutionPolicy RemoteSigned
Set-ExecutionPolicy : Windows PowerShell 已成功更新你的执行策略，但在更具体的作业域中定义的策略覆盖了该设置。由于发生覆盖，你的外壳程序将保留其当前的有效执行 
策略 Restricted。请键入“Get-ExecutionPolicy -List”以查看你的执行策略设置。有关详细信息，请参阅“Get-Help Set-ExecutionPolicy”。
所在位置 行:1 字符: 1
+ Set-ExecutionPolicy RemoteSigned
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (:) [Set-ExecutionPolicy], SecurityException
    + FullyQualifiedErrorId : ExecutionPolicyOverride,Microsoft.PowerShell.Commands.SetExecutionPolicyCommand
```

还是没有变化

```
# not working
PS F:\Github\Python\HeadFirstPython\HeadFirstPython> Get-ExecutionPolicy
Restricted
```

**看看有哪些作业域**

```
PS F:\Github\Python\HeadFirstPython\HeadFirstPython> Get-ExecutionPolicy -List

        Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process       Undefined
  CurrentUser      Restricted
 LocalMachine    RemoteSigned
```

### 帮助 get-help Set-ExecutionPolicy

```
get-help Set-ExecutionPolicy    

名称
    Set-ExecutionPolicy
    
语法
    Set-ExecutionPolicy [-ExecutionPolicy] {Unrestricted | RemoteSigned | AllSigned | Restricted | Default | Bypass | Undefined} [[-Scope] {Process | Current 
    User | LocalMachine | UserPolicy | MachinePolicy}]  [<CommonParameters>]


别名
    无


备注
    Get-Help 在此计算机上找不到该 cmdlet 的帮助文件。它仅显示部分帮助。
        -- 若要下载并安装包含此 cmdlet 的模块的帮助文件，请使用 Update-Help。
        -- 若要联机查看此 cmdlet 的帮助主题，请键入: "Get-Help Set-ExecutionPolicy -Online" 或
           转到 https://go.microsoft.com/fwlink/?LinkID=113394。
```

（4）把当前用户的执行权限修改一下

```
Set-ExecutionPolicy RemoteSigned CurrentUser

Get-ExecutionPolicy
# RemoteSigned

Get-ExecutionPolicy -List
#         Scope ExecutionPolicy
#         ----- ---------------
# MachinePolicy       Undefined
#    UserPolicy       Undefined
#       Process       Undefined
#   CurrentUser    RemoteSigned
#  LocalMachine    RemoteSigned
```





 