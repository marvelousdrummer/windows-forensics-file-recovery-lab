# Reviewed forensic screenshot gallery

This directory contains **8 reviewed screenshots** selected from **26 captures** produced during the controlled Windows 11 forensic lab. The original experiment used synthetic files. Images were cropped to emphasize the recorded results, and the DMDE screenshot has a local host path redacted. See the [main README](../README.md#visual-evidence) for a side-by-side image gallery.

| File | What the screenshot documents |
| --- | --- |
| [`05_Recuva_One_File_Recovered.png`](05_Recuva_One_File_Recovered.png) | Recuva reported one fully recovered file. Content identity is checked separately in the adjacent SHA-256 screenshot. |
| [`06_Recuva_JPEG_SHA256_Match.png`](06_Recuva_JPEG_SHA256_Match.png) | PowerShell shows identical SHA-256 digests for the original and Recuva-recovered JPEG. |
| [`12_SDelete_Three_Pass_Execution.png`](12_SDelete_Three_Pass_Execution.png) | SDelete reports three passes and one deleted file. This alone is not proof that no historical copies remain. |
| [`20_PhotoRec_Original_ODT_SHA256_Match.png`](20_PhotoRec_Original_ODT_SHA256_Match.png) | The PhotoRec-recovered ODT matches an earlier unencrypted original, not the encrypted SDelete target. This is not proof of SDelete failure. |
| [`23_Encrypted_PDF_Baseline_SHA256.png`](23_Encrypted_PDF_Baseline_SHA256.png) | SHA-256 baseline for the preserved encrypted PDF. This image alone does not compare the recovered file against the backup. |
| [`26_DMDE_Deleted_Partition_File_Discovered.png`](26_DMDE_Deleted_Partition_File_Discovered.png) | DMDE displays the deleted NTFS volume and its 63,962-byte encrypted PDF. The image shows discovery, not a completed extraction. |
| [`24_ODT_Dictionary_Attack_Result.png`](24_ODT_Dictionary_Attack_Result.png) | The offline Python dictionary test finds the lab ODT password on candidate 6 of 8. |
| [`25_PDF_Four_Digit_Search_Result.png`](25_PDF_Four_Digit_Search_Result.png) | The four-digit numeric test finds the demo PDF password after 1,235 attempts in 4.29 seconds. |

## Interpretation cautions

- The DMDE screenshot shows **discovery** of the 63,962-byte encrypted PDF on the deleted partition. The subsequent extraction is described in [findings](../docs/findings.md), not shown in this screenshot.
- The PDF baseline-hash screenshot shows the preserved encrypted backup's SHA-256. It **does not independently display** a comparison to the recovered PDF.
- The ODT recovered after SDelete was an earlier **unencrypted original**. Its matching hash is not proof that SDelete failed on the different, encrypted target.
- A reported recovery operation is not a substitute for content or hash verification.

## Review checklist for future images

1. Crop or redact personal usernames, host filesystem paths, machine identifiers, account avatars, notifications, and unrelated desktop content.
2. Exclude copyrighted textbook pages, licensed lab instructions, and complete university assignment submissions.
3. Compare each screenshot's caption to exactly what is visible.
4. Do not publish disk images, recovered user documents, credentials, or evidence files without explicit review.
5. Record original and published filenames in [the evidence register](../docs/evidence-register.csv).
