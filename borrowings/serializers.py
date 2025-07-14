from rest_framework import serializers
from .models import Borrowing
from library_books.serializers import BookSerializer
from library.models import Book


class BorrowingSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), source='book', write_only=True)

    class Meta:
        model = Borrowing
        fields = ['id', 'user', 'book', 'book_id', 'borrow_date', 'expected_return_date', 'actual_return_date']
        read_only_fields = ['user', 'borrow_date', 'actual_return_date']

    def create(self, validated_data):
        user = self.context['request'].user
        book = validated_data['book']

        if book.inventory < 1:
            raise serializers.ValidationError("Book not available in inventory.")

        book.inventory -= 1
        book.save()

        borrowing = Borrowing.objects.create(user=user, **validated_data)
        return borrowing
