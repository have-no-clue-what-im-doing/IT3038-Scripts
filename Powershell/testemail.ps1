$Message = new-object Net.Mail.MailMessage 
$smtp = new-object Net.Mail.SmtpClient("smtp.gmail.com", 587) 
$smtp.Credentials = New-Object System.Net.NetworkCredential("brodericjduncan@gmail.com", "oeyjbuidjbrhdzco"); 
$smtp.EnableSsl = $true 
$smtp.Timeout = 400000  
$Message.From = "brodericjduncan2@gmail.com" 
$Message.To.Add("brodericjduncan@gmail.com") 
$smtp.Send($Message)