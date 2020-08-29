import win32com.client
import os

application = win32com.client.Dispatch('Outlook.Application')
namespace = application.GetNamespace('MAPI')

inboxID = 6
inboxFolder = namespace.GetDefaultFolder(inboxID)
moveToFolder = inboxFolder.Folders.Item('test')

for counter in range(inboxFolder.Items.Count, 0, -1):
    email = inboxFolder.Items.Item(counter)

    if email.Subject == 'test': # change this to the subject of your email
        attachments = []
        
        for attachment in email.Attachments:
            aName = email.SentOn.strftime("%m.%d.%Y") + ' - ' + attachment.FileName
            if not attachment.FileName.endswith('xlsx'):
                continue
               
            fileSaveLocation = os.path.join('C:/test/', aName)
            attachment.SaveAsFile(fileSaveLocation)
            attachments.append(fileSaveLocation)
            email.Move(moveToFolder)