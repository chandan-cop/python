<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Certificate</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 0;
            width: 29.7cm; /* A4 width in landscape */
            height: 21cm; /* A4 height */
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f7f7f7;
        }
        .certificate {
            border: 10px solid #333;
            background-image: url('certificate_bg.jpg');
            background-size: cover;
            padding: 20px;
            width: 100%;
            height: 100%;
            position: relative;
            text-align: center;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 0.5em;
        }
        h2 {
            font-size: 2em;
            margin: 1em 0;
        }
        p {
            font-size: 1.2em;
            margin: 0.5em 0;
        }
        .footer {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
        }
        .signature {
            margin-top: 50px;
            text-align: right;
        }
    </style>
</head>
<body>
    <div class="certificate">
        <div class="header">
            <img src="mtd.png" alt="Organization Logo" style="max-width: 200px;">
            <p style="color:blue; font-weight:bold;"> www.mtdn.co.in </p>
        </div>
        <h1>Certificate of Achievement</h1>
        <h3>This certifies that</h3>
        <p id="name_usn">
            <strong>
                ADITYA S KUDE (<span>2KE23CS007</span>)
            </strong>
        </p>
        <p>Has successfully completed the training and workshop of 5 days held in September 2024. The student completed the CRUD operations project that involved</p>
        <h4> Front end, Django as backend and Mysql as database. </h4>
        <p>Date: [18-12-2024]</p>
        <div class="signature">
            <img src="my_sign.jpg" width="150" style="margin-right:150px">
            <h5 style="margin-right:100px">Nithin Neelakanta Rao [MTD Founder]</h5>
        </div>
    </div>
</body>
</html>