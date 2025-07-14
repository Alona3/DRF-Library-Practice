from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Borrowing
from .serializers import BorrowingSerializer

class BorrowingViewSet(viewsets.ModelViewSet):
    serializer_class = BorrowingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Borrowing.objects.all()

        if not user.is_staff:
            queryset = queryset.filter(user=user)

        is_active = self.request.query_params.get('is_active')
        if is_active is not None:
            if is_active.lower() in ['true', '1']:
                queryset = queryset.filter(actual_return_date__isnull=True)
            elif is_active.lower() in ['false', '0']:
                queryset = queryset.filter(actual_return_date__isnull=False)

        user_id = self.request.query_params.get('user_id')
        if user.is_staff and user_id:
            queryset = queryset.filter(user__id=user_id)

        return queryset
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def return_book(self, request, pk=None):
        borrowing = self.get_object()
        if borrowing.actual_return_date is not None:
            return Response({"detail": "Borrowing already returned."}, status=status.HTTP_400_BAD_REQUEST)

        borrowing.actual_return_date = timezone.now().date()
        borrowing.save()
        book = borrowing.book
        book.inventory += 1
        book.save()

        return Response({"detail": "Book returned successfully."})