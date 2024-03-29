B
    ��e`  �               @   s:   d dl Zd dlmZ d dlmZmZ G dd� dej�ZdS )�    N)�settings)�
migrations�modelsc               @   s   e Zd ZdZe�ej�gZej	dde
jddddd�fde
jddd	�fd
e
jdd�fde
jdd�fde
�� fde
jdd�fde
jdd�fde
�� fde
jdd�fde
jdd�fde
jdd�fde
jdd�fde
jejj
jjejd�fgdddd
dgd�d�gZdS ) �	MigrationT�Seller�idF�ID)�auto_created�primary_key�	serialize�verbose_name�slug��   )�
max_length�unique�
first_name�d   )r   �	last_name�date_of_birth�email��   �phone�   �address�city�state�country�zip�
   �user)�	on_delete�to�Sellers�seller)r   �verbose_name_plural�db_table�ordering)�name�fields�optionsN)�__name__�
__module__�__qualname__�initialr   �swappable_dependencyr   �AUTH_USER_MODEL�dependencies�CreateModelr   �BigAutoField�	SlugField�	CharField�	DateField�
EmailField�	TextField�OneToOneField�django�db�deletion�CASCADE�
operations� r>   r>   �iC:\Users\srava\Downloads\techbid-v2.1-store-item\techbid-master\backend\seller\migrations\0001_initial.pyr      s:   


r   )�django.db.models.deletionr9   �django.confr   �	django.dbr   r   r   r>   r>   r>   r?   �<module>   s   