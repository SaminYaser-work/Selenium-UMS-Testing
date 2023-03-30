<?php 

require('header.php');require('../model/form.php');

if(!isset($_REQUEST['upload']))
{
    ?>

    <form class="list" action="form.php" method="post" enctype="multipart/form-data">
        <div class="heading"><p>Form List</p></div>


            <?php
            
            $data = getAllform();

            ?>

            <table class="list">
                <tr><th>Form</th><th>Download</th><th>Delete</th></tr>
                <tr>
                            

                </tr>

            <?php


            //for($i=0; $i<sizeof($infoArray); $i++)
            while($infoArray =  mysqli_fetch_assoc($data))
            
            {
                $arr = explode("../image/",$infoArray['name']);
                //echo $arr[2];
                
                ?>
                                <tr>
                                    <td><?php echo $arr[1];?></td>
                                    <td><?php echo '<a href='.$infoArray['name'].' download>Download</a>';?></td>
                                    <td><?php echo '<a href=form.php?did='.$infoArray['id'].'>Delete</a>'; ?></td>
                                </tr>
                <?php     
            }

            
            ?>
                            <tr class="center">
                                <td><input id='file' type="file" name="uploadedFile" onchange="checkForm()"></td>
                                <td><input id="submit" type="submit" name="upload" value="Add Form" hidden></td>
                            </tr>
        </table>
    </form>
    <?php

}

else if (isset($_REQUEST['upload']))
{
    require('../model/functions.php');

    $temp = $_FILES['uploadedFile']['tmp_name'];
    $real = $_FILES['uploadedFile']['name'];
    $img_path = moveFile($temp, $real);
    if($img_path)
    {
        if(addform($img_path))
        {
            header('location:form.php');
        }

    }
}

else if(isset($_GET['did'])) //delete is clicked-----
{
    //did = delete identity
    $status = deleteForm($_GET['did']); //did = delete identity


    if($status)
    {
            header('location:form.php');
    
    }
}






?>