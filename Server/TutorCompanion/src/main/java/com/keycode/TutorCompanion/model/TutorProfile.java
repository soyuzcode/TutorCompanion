package com.keycode.TutorCompanion.model;

import com.fasterxml.jackson.annotation.JsonBackReference;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.MapsId;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "tutor_profiles")
public class TutorProfile {

    @Id
    @Column(name = "user_id")
    private Long userId;

    @OneToOne
    @MapsId
    @JsonBackReference
    @JoinColumn(name = "user_id")
    private User user;

    private Double rating;

    @Column(name = "approved_hours")
    private Integer approvedHours;

    public TutorProfile() {
    }

    public TutorProfile(User user, Double rating, Integer approvedHours) {
        this.user = user;
        this.rating = rating;
        this.approvedHours = approvedHours;
    }

    public Long getUserId() {
        return userId;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public Double getRating() {
        return rating;
    }

    public void setRating(Double rating) {
        this.rating = rating;
    }

    public Integer getApprovedHours() {
        return approvedHours;
    }

    public void setApprovedHours(Integer approvedHours) {
        this.approvedHours = approvedHours;
    }
}