function! Crypt()
    let wiki_path='~/adrian-cryptwiki'
    exe 'cd' wiki_path

    let dirs = readfile(".cryptfile")
    let dlen = len(dirs)
    let folders_exist = 0
    for i in dirs
        if isdirectory(i)
            let folders_exist += 1
        endif
    endfor

    if folders_exist != dlen
        echoerr 'ERROR [.cryptfile]: Folders specified do not exist. Try again.'
        return -1
    endif

    let folders_that_contain_files = 0
    let encrypted_file_count = 0
    let file_count = 0
    for i in dirs
        exe 'cd' wiki_path . '/' . i

        let files = split(globpath('.', '**'), '\n')

        if len(files) == 0
            echoerr 'ERROR [.cryptfile]: Input folder "' . wiki_path . '/' . i . '" is empty. Modify .cryptfile and try again.'
            return -1
        endif

        let file_count += len(files)
        for f in files
            if isdirectory(f)
                let file_count -= 1
            else
                let sp = split(f, '\.')
                let ext = sp[-1]
                if ext == "gpg"
                    let encrypted_file_count += 1
                endif
            endif
        endfor
    endfor

    if encrypted_file_count == 0
        exec 'cd' wiki_path
        execute 'silent !python crypt.py -e'
        echo "Wiki encrypted according to .cryptfile"
    elseif encrypted_file_count != file_count
        echoerr 'Error [encryption]: A .cryptfile directory contains some unencrypted files. Cannot run decryption process.'
        return -1
    else
        exec 'cd' wiki_path
        execute 'silent !python crypt.py -d'
        echo "Wiki decrypted according to .cryptfile"
    endif
endfunction
