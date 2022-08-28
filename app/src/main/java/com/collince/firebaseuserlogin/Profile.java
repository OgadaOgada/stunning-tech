package com.collince.firebaseuserlogin;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class Profile extends AppCompatActivity {

    private FirebaseUser user;
    private DatabaseReference reference;
    private String userID;
    private Button logoutButton;
    FirebaseAuth mAuth;

    private TextView fullname, age, email,welcome;
    private ProgressBar progressBar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);
        mAuth = FirebaseAuth.getInstance();

        logoutButton = findViewById(R.id.logoutBtn);

        logoutButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                FirebaseAuth.getInstance().signOut();
                startActivity(new Intent(getApplicationContext(),MainActivity.class));
            }
        });

        user = mAuth.getCurrentUser();
        reference = FirebaseDatabase.getInstance().getReference("Users");
        userID = user.getUid();
        fullname = findViewById(R.id.fullname);
        age = findViewById(R.id.age);
        email = findViewById(R.id.email);
        welcome = findViewById(R.id.welcome);

//        retrieving user details
        reference.child(userID).addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                User userprofile = snapshot.getValue(User.class);

                if(userprofile != null){
                    String fullnamestr = userprofile.fullname;
                    String agestr = userprofile.age;
                    String emailstr = userprofile.email;

                    welcome.setText("Welcome, "+fullnamestr+"!");
                    fullname.setText("Full name: "+fullnamestr);
                    age.setText("Age: "+agestr);
                    email.setText("Email address: "+emailstr);
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Toast.makeText(getApplicationContext(),"An error occured",Toast.LENGTH_LONG).show();
            }
        });

    }
}