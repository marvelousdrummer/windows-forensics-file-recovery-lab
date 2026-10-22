# Lab findings and evidence assessment

## Evidence handling

- All experiments used controlled, synthetic files in a Windows 11 VM.
- The Windows OS virtual disk was kept separate from an 8 GiB GPT-formatted evidence disk.
- Preserved originals and encrypted backups enabled SHA-256 comparisons.
- To investigate the deleted partition without repeatedly triggering guest disk-read errors, the active VirtualBox evidence-disk snapshot was cloned into a standalone VDI, then converted to an 8 GiB RAW image. DMDE examined the RAW image on the host.

## Experiment A: Shift+Delete and Recuva

A test JPEG was deleted using Shift+Delete. Recuva recovered one matching JPEG. SHA-256 of the recovered JPEG equaled its original backup (`8442364DD0455F2C6E1D2236DFA0FA669C87D5392B1831FA45DC8A76FA722875`).

**Assessment:** Ordinary deletion did not erase the JPEG's contents under these conditions.

## Experiment B: Windows cipher /w

After deleting the test JPEG, `cipher /w` was used to overwrite the volume's free space. Recuva's standard scan and deep scan returned no matching JPEG, and a subsequent PhotoRec recovery attempt did not locate it.

**Assessment:** No recovery through the methods tested. This does not prove that all historical copies, backups, shadow copies, or other residual artifacts have been removed.

## Experiment C: SDelete and prior data remnants

The encrypted ODT working copy was the target of `sdelete64.exe -p 3`. A later Recuva deep scan and PhotoRec search recovered an **unencrypted** ODT with SHA-256 matching the earlier unencrypted original (`AB64A389FB8EF005DE0B3B51F18D0E08BF365F9613428B0DCDB44774C7E3488A`). The encrypted backup had a **different** SHA-256 (`012AE17E442844B8324F74667C54E60E5D1C8E76E0D35C5B95EABA4E292F8915`).

**Assessment:** The tests recovered a prior unencrypted document version, not a verified copy of the file SDelete targeted. It would be incorrect to describe this as proven SDelete failure.

## Experiment D: Deleted NTFS partition

DiskPart deleted an NTFS partition that had contained a 63,962-byte encrypted PDF. TestDisk found the partition at LBA `8,421,376`–`16,773,119`, but guest access errors interrupted further analysis. VirtualBox logged an invalid read attempt at offset `8,589,934,592`, the first byte beyond the 8 GiB disk's range. After cloning the image and converting it to RAW, DMDE found `CYB451_PARTITION` and recovered `Top Secret Password Is Not 1234.pdf`. The PDF still requested its original test password and opened correctly.

The recovered PDF's SHA-256 matched the preserved encrypted backup:

`81C61585B64C201BC4FE156EDD0CE87ACDFDF22F6AE640E8695D2D573B1062C4`

**Assessment:** The test demonstrates recovery from a deleted partition without rebuilding its original partition table in place.

## Experiment E: Weak document passwords

- **ODT:** LibreOffice's encrypted file reported AES-256-GCM and Argon2id metadata. An older `libreoffice2john.py` did not recognize the encryption format. An eight-entry offline dictionary tested with Python and `odfdecrypt` recovered `password123` on the sixth attempt, producing a file that opened without a password.
- **PDF:** Python and `pypdf` tested the 10,000 four-digit combinations (`0000`–`9999`) and found `1234` on attempt 1,235, after 4.29 seconds in the recorded run.

**Assessment:** These results reflect intentionally weak laboratory passwords; they are not attacks on the underlying encryption algorithms.

## General limitations

- This is a teaching experiment with synthetic evidence, not a validated forensic tool benchmark.
- The virtual storage environment and scanning configuration matter; results may differ on real SSDs, HDDs, and other file systems.
- A failure to recover a file is not proof of permanent erasure.
- Hash equality supports byte-for-byte identity between compared files, but cannot alone replace a full acquisition or chain-of-custody process.
- The script files in this repository are refactored demonstrations; their refactored copies have not been separately validated against the original VM test files.
