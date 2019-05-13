# appsquatting

Domain squatting, a well-known adversarial tactic that attackersregister domain names that are purposefully similar to popular do-mains, had been observed and studied for decades. Recent studiessuggested that squatting-like attacks have been penetrated to various problem spaces. We demonstrates that squattingbehaviors are also prevalent in the mobile app ecosystem with adifferent manner, which we called “App Squatting”. Specifically,attackers may release app with identifiers (e.g., app name, pack-age name or developer name) that are confusingly similar to thosebelonging to popular apps or large Internet brands. 

We summarize 11 deformation models for app squatting. In particular, we propose and implement a tool named “AppCrazy”, which is capable of automatically generating variations of app identifiers.

Squatting-generation Models:

1、Mutation-based Models. 

    (1) Case Substitution: Replace an uppercase character with a lowercase one (or vice versa), e.g., “Facebook” into “facebook”.

    (2) Vowel Character Insertion: Insert another vowel character after a vowel character, e.g., “Facebook” into “Faceebook”.

    (3) Vowel Character Deletion: Delete one or more vowel characters, e.g., “Facebook” into “Facbook”.

    (4) Vowel Character Substitution: Replace a vowel characters with other four vowel characters, e.g., “Facebook” into “Fecebook”.

    (5) Double Character Insertion: Insert a same character between two consecutive identical characters, e.g., “Facebook” into “Faceboook”.

    (6) Double Character Deletion: Delete one or two characters who are the consecutive identical characters, e.g., “Facebook” into “Facebok”, and “Facebook” into “Facebk”.

    (7) Punctuation Substitution: Replace punctuation with other ones ( including space, underscore and dot), e.g., “com.facebook.katana” into “com.facebook_katana”.

    (8) Punctuation Deletion: Delete a punctuation (including space, underscore and dot), e.g., “com.facebook.katana” into “com.facebookkatana”.

    (9) Common Misspelling Mistakes Substitution: Replace specific characters with common misspelling mistakes. e.g., “Facebook” into “Faceb00k”.

2、Combosquatting Generation Models. 

    (1) String Expansion: Insert characters before or after the identifier name, e.g., “Facebook” into “Facebook1”.
    
    (2) String Rearrangement: Split the string into elements based on character dot, and rearrangement the elements, e.g., “com.facebook.katana” into “com.katana.facebook”. Specifically, rearranged strings that are composed of commonnames in Android will be discarded. e.g., “com.android”, “com.google”, “com.game”
    
3、AppCrazy Tools 

    Generating potential squatting appname and packagename,Supports the following Squatting Generation Models:
    
    usage:
	
    AppCrazy Usage Example:
    (1) AppCrazy.py -a example -p com.example
    print result on the screen.
	
![image](https://github.com/squattingapp/AppCrazy/raw/master/Screenshot/screenshot1.jpg)
		
    (2) AppCrazy.py -a example -p com.example -f ./example.txt
    write result into .txt file.

![example](https://github.com/squattingapp/AppCrazy/raw/master/Screenshot/screenshot2.jpg)

Result File.

    (1)fake_app.xlsx: Fake apps collected by leveraging AppCrazy to 500 popular apps in Google Play.
    (2)squatting_app.xlsx: Squatting apps collected by leveraging AppCrazy to 500 popular apps in Google Play.
    
    column1: app name;
    column2: original app name;
    column3: package name;
    column4: original package name;
    column5: developer name;
    column6: original developer name;
    column7: apk_md5;
    column8: apk_sha256;
    column9: apk_version;
    column10: apk_size(bytes);
    
