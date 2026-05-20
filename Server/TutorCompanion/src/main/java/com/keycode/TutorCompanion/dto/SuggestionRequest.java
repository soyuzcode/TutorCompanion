package com.keycode.TutorCompanion.dto;

public record SuggestionRequest(

        Long studentId,
        Long tutorId,
        Long subjectId,

        String topic,
        String message

) {
}