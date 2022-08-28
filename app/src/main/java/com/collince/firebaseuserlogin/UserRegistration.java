package com.collince.firebaseuserlogin;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.FirebaseDatabase;

public class UserRegistration extends AppCompatActivity implements View.OnClickListener{

    private TextView banner, registration;
    private EditText editTextfullname, editTextage, editTextemail, editTextpassword;
    private ProgressBar progressbar;

    private FirebaseAuth mAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_registration);
        mAuth = FirebaseAuth.getInstance();

        banner = findViewById(R.id.textView);
        banner.setOnClickListener(this);

        registration = (Button) findViewById(R.id.registerBtn);
        registration.setOnClickListener(this);

        editTextfullname = findViewById(R.id.fullname);
        editTextage = findViewById(R.id.age);
        editTextemail = findViewById(R.id.email);
        editTextpassword = findViewById(R.id.password);

        progressbar = findViewById(R.id.progressBar);
    }

    @Override
    public void onClick(View view) {
        switch (view.getId()) {
            case (R.id.textView):
                startActivity(new Intent(this, MainActivity.class));
                break;
            case (R.id.registerBtn):
                registerUser();
                break;

        }
    }

    private void registerUser() {
        String namestr = editTextfullname.getText().toString().trim();
        String agestr = editTextage.getText().toString().trim();
        String emailstr = editTextemail.getText().toString().trim();
        String passwordstr = editTextpassword.getText().toString().trim();

        if(namestr.isEmpty()){
            editTextfullname.setError("Full name is required");
            editTextfullname.requestFocus();
            return;
        }
        if(agestr.isEmpty()){
            editTextage.setError("Age is required");
            editTextage.requestFocus();
            return;
        }
        if(emailstr.isEmpty()){
            editTextemail.setError("Email is required");
            editTextemail.requestFocus();
            return;
        }
        if(!Patterns.EMAIL_ADDRESS.matcher(emailstr).matches()){
            editTextemail.setError("Please provide a valid email!");
            editTextemail.requestFocus();
            return;
        }

        if(passwordstr.isEmpty()){
            editTextpassword.setError("Password is required");
            editTextpassword.requestFocus();
            return;
        }
        int passlength = 6;
        if(passwordstr.length()<passlength){
            editTextpassword.setError("Min password length is "+passlength+" characters!");
            editTextpassword.requestFocus();
            return;
        }
        progressbar.setVisibility(View.VISIBLE);
        mAuth.createUserWithEmailAndPassword(emailstr,passwordstr)
                .addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        if(task.isSuccessful()){
                            User user = new User(namestr,agestr,emailstr);

                            FirebaseDatabase.getInstance().getReference("Users")
                                    .child(FirebaseAuth.getInstance().getCurrentUser().getUid())
                                    .setValue(user).addOnCompleteListener(new OnCompleteListener<Void>() {
                                        @Override
                                        public void onComplete(@NonNull Task<Void> task) {
                                            if(task.isSuccessful()){
                                                Toast.makeText(getApplicationContext(),"Registered successfully, now login.",Toast.LENGTH_LONG).show();
                                                progressbar.setVisibility(View.GONE);
                                                startActivity(new Intent(getApplicationContext(),MainActivity.class));
                                            }
                                        }
                                    });
                        }

                    }
                })
                .addOnFailureListener(new OnFailureListener() {
                    @Override
                    public void onFailure(@NonNull Exception e) {
                        Toast.makeText(getApplicationContext(),e.getMessage(),Toast.LENGTH_LONG).show();
                        progressbar.setVisibility(View.GONE);
                    }
                });
    }
}